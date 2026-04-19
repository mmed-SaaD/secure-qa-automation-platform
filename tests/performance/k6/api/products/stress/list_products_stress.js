import http from 'k6/http';
import {check, sleep} from 'k6';

import { commonJsonChecks, productsListChecks } from '../helpers/checks.js';
import { BASE_URL, THINKING_TIME } from '../helpers/config.js';
import { buildGetParams } from '../helpers/requests.js';

export const options = {
    scenarios : {
        products_list : {
            executor : 'ramping-vus',
            startVUs : 0,
            stages : [
                {duration : '30s', target : 10},
                {duration : '30s', target : 20},
                {duration : '30s', target : 250},
                {duration : '30s', target : 500},
                {duration : '30s', target : 1000},
                {duration : '30s', target : 1750},
                {duration : '30s', target : 0},
            ],
            gracefulRampDown : '10s',
        },
    },
    thresholds : {
        http_req_failed : [
            {threshold : 'rate<0.05'},
        ],
    },
};

const ENDPOINT = __ENV.ENDPOINT || "/products";

export default function(){
    const url = `${BASE_URL}${ENDPOINT}`;
    const params = buildGetParams('GET /products', 'list_products');
    const res = http.get(url, params);

    check(res, {
        ...commonJsonChecks(),
        ...productsListChecks(),
    });
    sleep(THINKING_TIME);
}
