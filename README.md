# merge-queue-experiments
Sandbox for messing around with GitHub merge queues

## What are merge queues?

Merge queues are an automated way to control releases into your default branch. They are a way to ensure that your default branch is always releasable, and that you can control the rate at which changes are released.

## Experiments

The goal of this repo is to experiment and document the sharp edges associated with running a git flow style repository
with merge queues. The major benefit we get from this style is that we can test a group of changes together before
releasing them into production. This is especially useful for changes that are not backwards compatible.
