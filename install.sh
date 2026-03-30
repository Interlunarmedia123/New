#!/usr/bin/env bash
set -euo pipefail

# Claude Code CLI Installer
# Usage: curl -fsSL https://claude.ai/install.sh | bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

info()    { printf "${BLUE}[info]${NC}  %s\n" "$*"; }
success() { printf "${GREEN}[ok]${NC}    %s\n" "$*"; }
warn()    { printf "${YELLOW}[warn]${NC}  %s\n" "$*"; }
error()   { printf "${RED}[error]${NC} %s\n" "$*" >&2; }

die() {
  error "$*"
  exit 1
}

# ── OS / arch detection ──────────────────────────────────────────────────────
OS="$(uname -s)"
ARCH="$(uname -m)"

case "$OS" in
  Linux)  PLATFORM="linux" ;;
  Darwin) PLATFORM="darwin" ;;
  *) die "Unsupported operating system: $OS" ;;
esac

info "Detected platform: $PLATFORM ($ARCH)"

# ── Dependency checks ────────────────────────────────────────────────────────
check_cmd() { command -v "$1" &>/dev/null; }

require_node() {
  if check_cmd node; then
    NODE_VERSION="$(node --version 2>/dev/null | sed 's/v//')"
    MAJOR="${NODE_VERSION%%.*}"
    if [ "$MAJOR" -lt 18 ]; then
      die "Node.js >= 18 is required (found v${NODE_VERSION}). Please upgrade: https://nodejs.org"
    fi
    success "Node.js v${NODE_VERSION} found"
  else
    die "Node.js is required but was not found. Install it from https://nodejs.org and re-run this script."
  fi
}

require_npm() {
  if check_cmd npm; then
    NPM_VERSION="$(npm --version 2>/dev/null)"
    success "npm v${NPM_VERSION} found"
  else
    die "npm is required but was not found. It is bundled with Node.js – please (re-)install Node.js from https://nodejs.org"
  fi
}

# ── Installation ─────────────────────────────────────────────────────────────
install_via_npm() {
  info "Installing @anthropic-ai/claude-code via npm…"
  npm install -g @anthropic-ai/claude-code
  success "Claude Code installed successfully!"
}

install_via_brew() {
  info "Installing Claude Code via Homebrew…"
  brew install anthropic/tap/claude-code
  success "Claude Code installed successfully!"
}

# ── Main ─────────────────────────────────────────────────────────────────────
main() {
  printf "\n"
  printf "  ██████╗██╗      █████╗ ██╗   ██╗██████╗ ███████╗\n"
  printf " ██╔════╝██║     ██╔══██╗██║   ██║██╔══██╗██╔════╝\n"
  printf " ██║     ██║     ███████║██║   ██║██║  ██║█████╗  \n"
  printf " ██║     ██║     ██╔══██║██║   ██║██║  ██║██╔══╝  \n"
  printf " ╚██████╗███████╗██║  ██║╚██████╔╝██████╔╝███████╗\n"
  printf "  ╚═════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝\n"
  printf "                                           Code CLI\n"
  printf "\n"

  # Prefer Homebrew on macOS when available
  if [ "$PLATFORM" = "darwin" ] && check_cmd brew; then
    install_via_brew
  else
    require_node
    require_npm
    install_via_npm
  fi

  # Verify the binary is reachable
  if check_cmd claude; then
    CLAUDE_VERSION="$(claude --version 2>/dev/null || true)"
    printf "\n"
    success "claude ${CLAUDE_VERSION} is ready."
    printf "\n"
    info "Get started: claude"
    info "Docs:        https://docs.anthropic.com/claude-code"
    printf "\n"
  else
    warn "Installation complete, but 'claude' was not found in PATH."
    warn "You may need to restart your shell or add npm's global bin directory to PATH:"
    warn "  $(npm bin -g 2>/dev/null || echo '~/.npm-global/bin')"
  fi
}

main "$@"
