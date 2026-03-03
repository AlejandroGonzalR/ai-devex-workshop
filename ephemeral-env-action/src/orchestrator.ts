import {composeUp, composeDown} from './docker';
import {estimateCost, recordStart} from './cost';

export async function up(pr: string) {
  const project = `preview-${pr}`;

  await composeUp(project, pr);
  await recordStart(pr);

  const url = `http://pr-${pr}.localhost`;

  console.log(`Preview ready at ${url}`);

  return url;
}

export async function down(pr: string) {
  const project = `preview-${pr}`;

  await composeDown(project);
  await estimateCost(pr);
}
