# Take all the versions verified on DEV to QA env. This can be merge/check-in/auto/manual.
cp "/Users/ishwargalane/workspace/argocd-test/multiappmultienv/base/release.conf" "/Users/ishwargalane/workspace/argocd-test/multiappmultienv/overlays/qa/release.conf"
cp "/Users/ishwargalane/workspace/argocd-test/multiappmultienv/base/deploy.py"    "/Users/ishwargalane/workspace/argocd-test/multiappmultienv/overlays/qa/deploy.py"

# Update version tags in overlay yamls, so that the ArgoCD can pick up the change.
cd "/Users/ishwargalane/workspace/argocd-test/multiappmultienv/overlays/qa"
python3 deploy.py
