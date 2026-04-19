export function buildGetParams(name, endpoint) {
  return {
    tags: {
      name,
      endpoint,
    },
  };
}