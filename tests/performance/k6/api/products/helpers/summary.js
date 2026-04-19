export function buildSummary(data, label = 'k6 Test Summary') {
  return {
    stdout: `
=== ${label} ===
checks rate        : ${data.metrics.checks?.values?.rate ?? 'n/a'}
http fail rate     : ${data.metrics.http_req_failed?.values?.rate ?? 'n/a'}
http avg duration  : ${data.metrics.http_req_duration?.values?.avg ?? 'n/a'} ms
http p95 duration  : ${data.metrics.http_req_duration?.values?.['p(95)'] ?? 'n/a'} ms
`,
    'summary.json': JSON.stringify(data, null, 2),
  };
}