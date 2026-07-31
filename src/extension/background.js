// VaultTube background service worker.

const NATIVE_HOST_NAME = "com.vaulttube.host";

function connectToHost() {
  return chrome.runtime.connectNative(NATIVE_HOST_NAME);
}
