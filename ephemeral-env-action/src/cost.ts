import fs from 'fs';

/*
$0.002 sstimated cost per minute refering Actions runner pricing
for Linux 1-core (x64)

For more information, please check:
https://docs.github.com/en/billing/reference/actions-runner-pricing
*/
const RATE = 0.002;

export async function recordStart(pr: string) {
  fs.writeFileSync(`.preview-${pr}`, Date.now().toString());
}

export async function estimateCost(pr: string) {
  const start = Number(fs.readFileSync(`.preview-${pr}`, 'utf8'));
  const end = Date.now();

  const minutes = Math.floor((end - start) / 60000);
  const cost = minutes * RATE;

  console.log(`
  ============= Preview Cost =============
  PR: ${pr}
  Uptime: ${minutes} min
  Cost: $${cost.toFixed(4)}
  ========================================
  `);

  fs.unlinkSync(`.preview-${pr}`);
}
