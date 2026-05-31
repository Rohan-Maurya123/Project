const validateMiddleware = (
  req,
  res,
  next
) => {
  next();
};

module.exports = validateMiddleware;