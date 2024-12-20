{ pkgs }: {
  deps = [
    pkgs.gdb
    pkgs.glibcLocales
    pkgs.glibc
    pkgs.nodejs-16_x
    pkgs.sudo
    pkgs.bind.dnsutils
    pkgs.iputils
    pkgs.systemd
    pkgs.nodePackages.prettier
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
  ];
}