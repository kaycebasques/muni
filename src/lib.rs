// https://developer.mozilla.org/en-US/docs/WebAssembly/Rust_to_wasm
// https://rustwasm.github.io/wasm-bindgen/examples/fetch.html

use wasm_bindgen::prelude::*;

#[wasm_bindgen]
extern {
    pub fn alert(s: &str);
}

#[wasm_bindgen]
pub fn greet(name: &str) {
    alert(&format!("Hello, {}!", name));
}
