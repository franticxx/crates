@echo off

cd %1

cargo login %2 --registry crates-io

(
echo [package]
echo name = "%1"
echo version = "0.1.0"
echo edition = "2021"
echo license = "MIT"
echo description = "%1"
echo repository = "http://example.com"
)>Cargo.toml

cargo publish --registry crates-io --allow-dirty

exit