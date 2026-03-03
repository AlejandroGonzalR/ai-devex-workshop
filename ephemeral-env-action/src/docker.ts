import * as exec from '@actions/exec';

export async function composeUp(project: string, pr: string) {
  await exec.exec('docker', [
    'compose',
    '-p',
    project,
    '-f',
    'infra/docker-compose.preview.yml',
    'up',
    '-d',
    '--build',
  ], {
    env: {PR_NUMBER: pr},
  });
}

export async function composeDown(project: string) {
  await exec.exec('docker', [
    'compose',
    '-p',
    project,
    '-f',
    'infra/docker-compose.preview.yml',
    'down',
    '-v',
  ]);
}
