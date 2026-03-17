
Git History

<img src="./media/git-icon-logo-svgrepo-com.svg" width="500" height="500" />


Note:

- Intro:

# Stakeholder

- Release Engineer
- Quality Assurance
- DevSecOps
- Maintainer
- Developer

## Release Engineer

- Pick and pin the source version for a release
- Create the changes section within release notes

## Quality Assurance

- Determine which commits constitute a release
- Verify review signoffs of all commits that contribute to a release
- Verify that authors, committers and reviewers have confirmed QM that they
  follow all QM policies (SOP)

## DevSecOps

- Verify that only trusted source (composed only of verified commits) is used
  for production/release build

## Maintainer

- Trace down bugs as fast as possible
- Apply bugfixes on all supported/maintained branches

## Developer

- Understand where to base new work on

# Producer

... of git history are

- Developer
- Maintainer
- Release Engineer

# Requirements

- Small atomic commits
- Single topic, single scope
- Signoff
- PGP secured commit for authenticity
- Self-contained commits
- No diamonds - long chain
- Enforced branch strategy

# Workshop Part

# Signing

- commits, tags
- with PKI (pgp/ssh) ==> "verified commits"

## Signing - embedded in commit

```
tree <hash>
parent <hash>
author ...
committer ...
gpgsig --BEGIN PGP SIGNATURE--

--END PGP SIGNATURE--
<commit message>
```

## Crypto - by the last committer

```
Signed-off-by: Author
Reviewed-by: Reviewer
Acked-by: Maintainer
Signed-off-by: Maintainer
```

## What is sign-off?

is a leagal statement:
(Developer Certificate of Origin) = DCO
no cryptography

# Commit

Small atomic commits
- One topic
- One scope
[https://conventionalcommit.org](https://conventionalcommit.org)

Note:
- check the web side for update e.g. breaking changes
- e.g. for filtering feat: und fix: for release notes
- precommit, commitizen,

## Commits - Support/Checks

- [Precommit](https://pre-commit.com)
  - [Precommit - rust alternative](https://github.com/j178/prek)
- [Commitizen](https://commitizen-tools.github.io/commitizen/)
- [conventional-changelog](https://github.com/conventional-changelog/conventional-changelog)

# Exercise - Maintainer find Bug

- Apply `git bisect` [manpage](https://git-scm.com/docs/git-bisect)
- Apply `git blame`  [manpage](https://git-scm.com/docs/git-blame)

# Exercise - Split last Commit

- Checkout branch `split-last-commit`
- Run `git log -1 --name-only --oneline` to see the last commit
  modifying two files `a.txt` and `b.txt`
- Task: Split into two commits each modifying one file each

## Split last Commit - Hints

Use the following git commands
```
git checkout
git commit
git revert
git rebase
```

## Split last Commit - Solution

```
Modify a and  b: &Delta; a, &Delta; b
==>
Modify a: &Delta; a
Modify b: &Delta; b
```

```
git checkout exercise-01
checkout HEAD^ -- b.txt # or git restore --source=HEAD^ b.txt
git commit -a -m "Modify a"
git revert HEAD --message "Modfy b"
git rebase -i HEAD~4 # squash HEAD~1 and HEAD~2

# Exercise - Sort in Review Fixes

# Exercise - Maintainer find Bug

