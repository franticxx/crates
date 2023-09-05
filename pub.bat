@echo off

cargo new %1 --lib

cd %1

rmdir /Q/S .git
del .git*


(
echo [package]
echo name = "%1"
echo version = "0.1.0"
echo edition = "2021"
echo license = "MIT"
echo description = "%1"
echo repository = "https://github.com/franticxx/crates/%1"
)>Cargo.toml

cargo publish --registry crates-io --allow-dirty

exit