export function commonJsonChecks() {
  return {
    'status is 200/201': (r) => [200,201].includes(r.status),
    'content-type is json': (r) =>
      String(r.headers['Content-Type'] || '').includes('application/json'),
  };
}

export function productsListChecks() {
  return {
    'response has non-empty products array': (r) => {
      try {
        const products = r.json('products');
        return Array.isArray(products) && products.length > 0;
      } catch (e) {
        return false;
      }
    },
  };
}

export function searchProductChecks(keyword) {
  return {
    'response has an array' : (r) => {
      try{
        return Array.isArray(r.json('products'));
      }catch (e){
        return false;
      }
    },
    'results are relevant or empty' : (r) => {
      try{
        const products = r.json("products");

        if(!Array.isArray(products)) return false;

        if(products.length === 0) return true;

        return products.some(p => String(p.title || '').toLowerCase().includes(keyword.toLowerCase()));
      }catch (e){
        return false;
      }
    }
  }
}

export function searchProductByIdChecks(product_id){
  return {
    'response is an object' : (r) => {
      try{
          const body = r.json();
          return typeof body === 'object' && body !== null;
      }catch (e){
        return false;
      }
    },
    'product has correct id' : (r) => {
      try{
          const body = r.json();
          return body.id === product_id
      }catch (e){
        return false;
      }
    }
  }
}

export function loginChecks(user_id) {
  return {
    'response has accessToken and refreshToken': (res) => {
      try {
        const body = res.json();
        return !!body?.accessToken && !!body?.refreshToken;
      } catch (e) {
        return false;
      }
    },

    'response accessToken is well formed': (res) => {
      try {
        const token = res.json()?.accessToken;
        if (!token || typeof token !== 'string') return false;

        const jwtRegex = /^[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+$/;
        return jwtRegex.test(token);
      } catch (e) {
        return false;
      }
    },

    'response has correct id': (res) => {
      try {
        return res.json()?.id === user_id;
      } catch (e) {
        return false;
      }
    }
  };
}

export function authUserChecks(user_id) {
  return {
    'response has correct id': (res) => {
      try {
        return res.json()?.id === user_id;
      } catch (e) {
        return false;
      }
    },

    'response has username': (res) => {
      try {
        return typeof res.json()?.username === 'string';
      } catch (e) {
        return false;
      }
    },

    'response has email': (res) => {
      try {
        return typeof res.json()?.email === 'string';
      } catch (e) {
        return false;
      }
    }
  };
}

export function assertProductAdded() {
  return {
    'response has server-added product id': (res) => {
      try {
        return res.json()?.id === 195;
      } catch (e) {
        return false;
      }
    }
  };
}