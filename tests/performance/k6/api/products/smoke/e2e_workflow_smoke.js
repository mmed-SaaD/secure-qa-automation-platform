import http from 'k6/http';
import {check, sleep} from 'k6';
import {Trend, Rate} from 'k6/metrics';

import { BASE_URL, THINKING_TIME } from '../helpers/config.js';
import { buildGetParams } from '../helpers/requests.js';
import { authUserChecks, commonJsonChecks, loginChecks, productsListChecks } from '../helpers/checks.js';

const productsDuration = new Trend('products_duration', true);
const productsContentValid = new Rate('products_content_valid');


export const options = {
  scenarios: {
    e2e_workflow_smoke: {
      executor: 'constant-vus',
      vus: 1,
      duration: '30s',
    },
  },
  thresholds: {
    http_req_failed: [{ threshold: 'rate==0', abortOnFail: true }],
    products_duration: [
      { threshold: 'p(95)<1500', abortOnFail: true },
      { threshold: 'avg<1000', abortOnFail: true },
    ],
    products_content_valid: [{ threshold: 'rate>0.99', abortOnFail: true }],
  },
};

const AUTH_ENDPOINT = __ENV.AUTH_ENDPOINT || "/auth/login";
const GET_AUTH_USER_ENDPOINT = __ENV.GET_AUTH_USER_ENDPOINT || "/auth/me";
const GET_AUTH_PRODUCTS = __ENV.GET_AUTH_PRODUCTS || "/auth/products";
const USERNAME = __ENV.USERNAME || "jamesd";
const PASSWORD = __ENV.PASSWORD || "jamesdpass";

export default function(){
    var url = `${BASE_URL}${AUTH_ENDPOINT}`;
    var params = {
       headers : {
        'Content-Type' : 'application/json',
       },
       ...buildGetParams('POST /auth/login', 'login_user'),  
    }
    const login_credentials = JSON.stringify({
        'username' : USERNAME,
        'password' : PASSWORD,
    });
    var res = http.post(url, login_credentials, params);
    const accessToken = res.json("accessToken");
    check(res, {
        ...commonJsonChecks(),
        ...loginChecks(4),
    });

    url = `${BASE_URL}${GET_AUTH_USER_ENDPOINT}`;
    params = {
        ...buildGetParams('GET /auth/me', 'get_logged_user_info'),
        headers : {
            'Content-Type' : 'application/json',
            'Authorization' : `Bearer ${accessToken}`
        },
    }
    res = http.get(url, params);
    check(res, {
        ...commonJsonChecks(),
        ...authUserChecks(4),
    });
    
    url = `${BASE_URL}${GET_AUTH_PRODUCTS}`;
    params = {
        ...buildGetParams('GET /auth/products', 'get_products_as_authorized_user'),
        headers : {
            'Content-Type' : 'application/json',
            'Authorization' : `Bearer ${accessToken}`
        },
    }
    res = http.get(url, params);
    check(res, {
        ...commonJsonChecks(),
        ...productsListChecks(),
    });
    sleep(THINKING_TIME);
}