<button
  onClick={async () => {
    await API.delete(`/items/${item._id}`);
    fetchItems();
  }}
  className="mt-2 bg-red-500 text-white px-3 py-1 rounded"
>
  Delete
</button>;
