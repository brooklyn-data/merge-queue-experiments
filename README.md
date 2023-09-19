# merge-queue-experiments
Sandbox for messing around with GitHub merge queues

## What are merge queues?

Merge queues are an automated way to control releases into your default branch. They are a way to ensure that your default branch is always releasable, and that you can control the rate at which changes are released.

## Experiments

The goal of this repo is to demonstrate two viable approaches to enforcing automated release windows using a combination
of GitHub actions and merge queues.

### Approach 1: Scripting

This approach uses a GitHub action to run a script that checks the current time and compares it to a release window. If
the current time is within the release window, the script will exit with a success code. If the current time is outside
of the release window the script will exit with a failure code.

The obvious drawback of this approach is that the check has to be performed on a cron schedule, which means that there
is an inherent delay between the time that the release window opens and the time that the release is actually performed.

### Approach 2: Artifacts

This approach uses a GitHub action to overwrite an artifact every time the release window opens and closes. Then, a CI
check is used to check the contents of the artifact when a PR is opened or updated to determine whether or not the PR
is a candidate for release.
