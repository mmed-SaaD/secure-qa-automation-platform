import http from 'k6/http';
import {check, sleep} from 'k6';

import { commonJsonChecks, searchProductByIdChecks } from '../helpers/checks.js';
import { BASE_URL, THINKING_TIME } from '../helpers/config.js';
import { buildGetParams } from '../helpers/requests.js';

export const options = {
    scenarios : {
        search_product : {
            executor : 'ramping-vus',
            startVUs : 0,
            stages : [
                {duration : '30s', target : 10},
                {duration : '30s', target : 20},
                {duration : '30s', target : 40},
                {duration : '30s', target : 60},
                {duration : '30s', target : 0},
            ],
            gracefulRampDown : '10s',
        },
    },
    thresholds : {
        http_req_failed : [
            {threshold : 'rate<0.01'},
        ],
        http_req_duration : [
            {threshold : 'p(95)<900'},
            {threshold : 'avg<600'},
        ],
        checks : [
            {threshold : 'rate>0.99'}
        ],
    },
};

const ENDPOINT = __ENV.ENDPOINT || "/products";
const PRODUCT_ID = Number(__ENV.PRODUCT_ID) || 7;


export default function(){
    const url = `${BASE_URL}${ENDPOINT}/${PRODUCT_ID}`;
    const params = buildGetParams('GET /products/:id', 'get_product_by_id');
    const res = http.get(url, params);

    check(res, {
        ...commonJsonChecks(),
        ...searchProductByIdChecks(PRODUCT_ID)
    });
    sleep(THINKING_TIME);
}
