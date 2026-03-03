import * as core from '@actions/core';
import {up, down} from './orchestrator';

async function run() {
  try {
    const action = core.getInput('action');
    const pr = core.getInput('pr-number');

    if (action === 'up') {
      const url = await up(pr);
      core.setOutput('preview-url', url);
    }

    if (action === 'down') {
      await down(pr);
    }
  } catch (err: any) {
    core.setFailed(err.message);
  }
}

run();
