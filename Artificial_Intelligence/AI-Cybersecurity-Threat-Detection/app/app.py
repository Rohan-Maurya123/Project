import streamlit as st
import pandas as pd
import joblib
import os
import time
import altair as alt
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Cyber Threat Detection", layout="wide", initial_sidebar_state="expanded")

st.title("🚨 AI Cybersecurity Threat Detection System")

# -------------------------------
# PATH SETUP
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))

model_path = os.path.join(ROOT_DIR, "models", "model.pkl")
columns_path = os.path.join(ROOT_DIR, "models", "columns.pkl")

# -------------------------------
# CHECK MODEL FILES
# -------------------------------
if not os.path.exists(model_path) or not os.path.exists(columns_path):
    st.error("❌ Model not found! Run 'python main.py' first.")
    st.stop()

# Load model and columns
model = joblib.load(model_path)
saved_columns = joblib.load(columns_path)

# -------------------------------
# KDD COLUMN NAMES (IMPORTANT)
# -------------------------------
columns = [
    "duration","protocol_type","service","flag","src_bytes","dst_bytes","land",
    "wrong_fragment","urgent","hot","num_failed_logins","logged_in","num_compromised",
    "root_shell","su_attempted","num_root","num_file_creations","num_shells",
    "num_access_files","num_outbound_cmds","is_host_login","is_guest_login",
    "count","srv_count","serror_rate","srv_serror_rate","rerror_rate",
    "srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate",
    "dst_host_count","dst_host_srv_count","dst_host_same_srv_rate",
    "dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate",
    "dst_host_srv_serror_rate","dst_host_rerror_rate",
    "dst_host_srv_rerror_rate"
]

st.markdown(
    """
<style>
  .block-container { padding-top: 2.5rem; padding-bottom: 2rem; }
  [data-testid="stSidebar"] > div:first-child {
    background: linear-gradient(180deg, #0b1220 0%, #0f1b2d 100%);
  }
  [data-testid="stSidebar"] * { color: #e9eef7 !important; }
  .hero {
    background: linear-gradient(90deg, rgba(15, 27, 45, 0.9), rgba(11, 18, 32, 0.9));
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 18px 18px;
    margin-bottom: 14px;
  }
  .hero h3 { margin: 0; color: #e9eef7; font-weight: 700; }
  .hero p { margin: 6px 0 0 0; color: rgba(233,238,247,0.78); }
  .card-row { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; margin-top: 10px; }
  .card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 14px 14px;
  }
  .card .k { font-size: 0.85rem; color: rgba(233,238,247,0.70); }
  .card .v { font-size: 1.55rem; font-weight: 800; color: #e9eef7; }
  .pill {
    display: inline-block;
    padding: 6px 10px;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.10);
    background: rgba(255,255,255,0.04);
    color: rgba(233,238,247,0.82);
    font-size: 0.85rem;
  }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero">
  <h3>Threat Detection Dashboard</h3>
  <p>Upload network traffic and instantly visualize detection results, distributions, and (when labels exist) a confusion matrix.</p>
</div>
""",
    unsafe_allow_html=True,
)

mode = st.sidebar.radio(
    "Mode",
    ["Upload & Detect", "Evaluate (test.csv)"],
    index=0,
)

threshold = st.sidebar.slider(
    "Threat threshold (probability)",
    min_value=0.05,
    max_value=0.95,
    value=0.50,
    step=0.05,
    help="If the model supports probabilities, values above this threshold are marked as threats.",
)

max_rows = st.sidebar.slider(
    "Max rows to process",
    min_value=500,
    max_value=5000,
    value=5000,
    step=500,
)

def predict_with_threshold(model_obj, features: pd.DataFrame, threshold_value: float) -> np.ndarray:
    if hasattr(model_obj, "predict_proba"):
        proba = model_obj.predict_proba(features)
        if proba.ndim == 2 and proba.shape[1] >= 2:
            return (proba[:, 1] >= threshold_value).astype(int)
    return model_obj.predict(features)

def align_features(raw_df: pd.DataFrame) -> pd.DataFrame:
    df_local = raw_df.copy()
    df_local = df_local.dropna(how="all")

    categorical_cols = [c for c in ["protocol_type", "service", "flag"] if c in df_local.columns]
    non_categorical_cols = [c for c in df_local.columns if c not in categorical_cols]

    for col in non_categorical_cols:
        df_local[col] = pd.to_numeric(df_local[col], errors="coerce")

    if categorical_cols:
        for col in categorical_cols:
            df_local[col] = df_local[col].astype(str)
        df_local = pd.get_dummies(df_local, columns=categorical_cols)

    remaining_object_cols = [c for c in df_local.columns if df_local[c].dtype == object]
    if remaining_object_cols:
        df_local = pd.get_dummies(df_local, columns=remaining_object_cols)

    df_local = df_local.fillna(0)
    feature_columns = [col for col in saved_columns if col != "label"]
    return df_local.reindex(columns=feature_columns, fill_value=0)

# -------------------------------
# FILE UPLOAD
# -------------------------------
uploaded_file = None
if mode == "Upload & Detect":
    uploaded_file = st.file_uploader("📂 Upload Network CSV File")

if mode == "Upload & Detect" and uploaded_file:

    try:
        # Load with correct column names
        df = pd.read_csv(uploaded_file, names=columns)

        st.write("### 📊 Raw Data Preview")
        st.dataframe(df.head(20))

        # -------------------------------
        # LIMIT DATA (PREVENT CRASH)
        # -------------------------------
        df = df.head(int(max_rows))

        progress = st.progress(0, text="Preparing features…")
        for i in range(3):
            time.sleep(0.05)
            progress.progress((i + 1) * 20, text="Preparing features…")

        X = align_features(df)
        progress.progress(70, text="Running model inference…")

        # -------------------------------
        # PREDICTION
        # -------------------------------
        predictions = predict_with_threshold(model, X, threshold)
        progress.progress(100, text="Done")

        df["Prediction"] = predictions

        # -------------------------------
        # DEBUG (VERY IMPORTANT)
        # -------------------------------
        st.write("### 🧪 Prediction Counts")
        st.write(pd.Series(predictions).value_counts())

        # -------------------------------
        # SHOW RESULTS
        # -------------------------------
        total_records = len(df)
        threat_count = int((df["Prediction"] == 1).sum())
        normal_count = total_records - threat_count

        st.markdown(
            f"""
<div class="card-row">
  <div class="card"><div class="k">Total Records</div><div class="v">{total_records}</div></div>
  <div class="card"><div class="k">Threats Detected</div><div class="v">{threat_count}</div></div>
  <div class="card"><div class="k">Threat Rate</div><div class="v">{(threat_count / max(total_records, 1)) * 100:.2f}%</div></div>
</div>
""",
            unsafe_allow_html=True,
        )

        # Show threats only
        threats = df[df["Prediction"] == 1]

        tabs = st.tabs(["Overview", "Threats", "Charts"])

        with tabs[0]:
            if threat_count > 0:
                st.error(f"⚠️ {threat_count} Potential Threats Detected!")
            else:
                st.success("✅ No Threats Detected")
            st.write("### 🔍 Sample Detection Results")
            st.dataframe(df.head(50))
            st.markdown(f"<span class='pill'>Threshold: {threshold:.2f}</span>", unsafe_allow_html=True)

        with tabs[1]:
            st.write("### 🚨 Detected Threats (Top 50)")
            st.dataframe(threats.head(50))

        with tabs[2]:
            st.write("### 📈 Prediction Distribution")
            chart_data = pd.DataFrame(
                {"Prediction": ["Normal (0)", "Threat (1)"], "Count": [normal_count, threat_count]}
            )
            bar = (
                alt.Chart(chart_data)
                .mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6)
                .encode(
                    x=alt.X("Prediction:N", sort=None),
                    y=alt.Y("Count:Q"),
                    color=alt.Color("Prediction:N", scale=alt.Scale(range=["#5aa9e6", "#ff4b4b"]), legend=None),
                    tooltip=["Prediction:N", "Count:Q"],
                )
                .properties(height=260)
            )
            st.altair_chart(bar, use_container_width=True)

            st.write("### 📊 Cumulative Threats (by row order)")
            cum = pd.DataFrame({"row": np.arange(total_records), "cum_threats": np.cumsum(df["Prediction"].values)})
            line = (
                alt.Chart(cum)
                .mark_line(interpolate="monotone", strokeWidth=3)
                .encode(x=alt.X("row:Q"), y=alt.Y("cum_threats:Q"), tooltip=["row:Q", "cum_threats:Q"])
                .properties(height=260)
            )
            st.altair_chart(line, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Error occurred: {e}")

if mode == "Evaluate (test.csv)":
    eval_cols = columns + ["label"]
    test_path = os.path.join(ROOT_DIR, "data", "test.csv")
    if not os.path.exists(test_path):
        st.error("❌ data/test.csv not found.")
        st.stop()

    df_test = pd.read_csv(test_path, names=eval_cols).head(int(max_rows))
    df_test = df_test.dropna()
    if "label" not in df_test.columns:
        st.error("❌ test.csv does not contain label column.")
        st.stop()

    df_test["label"] = df_test["label"].astype(str).str.replace(".", "", regex=False)
    df_test["label"] = df_test["label"].apply(lambda x: 0 if x == "normal" else 1)

    y_true = df_test["label"].astype(int).to_numpy()
    X_test = align_features(df_test.drop(columns=["label"]))
    y_pred = predict_with_threshold(model, X_test, threshold)

    total = len(y_true)
    threats = int((y_pred == 1).sum())
    st.markdown(
        f"""
<div class="card-row">
  <div class="card"><div class="k">Test Samples</div><div class="v">{total}</div></div>
  <div class="card"><div class="k">Predicted Threats</div><div class="v">{threats}</div></div>
  <div class="card"><div class="k">Threshold</div><div class="v">{threshold:.2f}</div></div>
</div>
""",
        unsafe_allow_html=True,
    )

    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    cm_df = pd.DataFrame(
        cm,
        index=["True Normal (0)", "True Threat (1)"],
        columns=["Pred Normal (0)", "Pred Threat (1)"],
    )

    st.write("### 🧩 Confusion Matrix")
    cm_long = cm_df.reset_index().melt(id_vars="index", var_name="Predicted", value_name="Count")
    cm_long = cm_long.rename(columns={"index": "Actual"})
    heat = (
        alt.Chart(cm_long)
        .mark_rect(cornerRadius=6)
        .encode(
            x=alt.X("Predicted:N", sort=None),
            y=alt.Y("Actual:N", sort=None),
            color=alt.Color("Count:Q", scale=alt.Scale(scheme="blues")),
            tooltip=["Actual:N", "Predicted:N", "Count:Q"],
        )
        .properties(height=260)
    )
    text = (
        alt.Chart(cm_long)
        .mark_text(fontSize=16, fontWeight="bold")
        .encode(x="Predicted:N", y="Actual:N", text="Count:Q", color=alt.value("#0b1220"))
    )
    st.altair_chart((heat + text), use_container_width=True)

    st.write("### 📄 Classification Report")
    report_dict = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    report_df = pd.DataFrame(report_dict).transpose()
    st.dataframe(report_df, use_container_width=True)
