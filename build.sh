uv run hello-amaranth
quartus_cpf -c -q 24.0MHz -g 3.3 -n p build/top.sof build/top.svf
sudo openFPGALoader -b de10lite build/top.svf
