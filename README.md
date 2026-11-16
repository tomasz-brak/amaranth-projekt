# Installation & Getting Started

By default, Amaranth compiles to Verilog, making it compatible with any toolchain that supports the language.

## Open-Source Toolchain (Arch Linux)

Install the required packages:

```bash
paru -S prjapicula-git nextpnr-git openfpgaloader
```
or
```bash
yay -S prjapicula-git nextpnr-git openfpgaloader
```

> **Note:** When building `nextpnr-git`, you can set the `DARCH` flag to only `himbaechel` in the `PKGBUILD`. The other architectures are not needed for this project and may cause build errors.

Install the latest development versions of Amaranth and board definitions using `uv`:

```bash
# Do this when setting your own project from groud up, this comes preconfigured in this template
uv add git+https://github.com/amaranth-lang/amaranth.git
uv add git+https://github.com/amaranth-lang/amaranth-boards.git
```

## Build & Flash

Once installed, building and flashing the bitstream to the board is straightforward:

```bash
uv run hello-amaranth
sudo openFPGALoader -b tangnano9k build/top.fs
```
