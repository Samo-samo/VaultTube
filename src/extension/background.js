// VaultTube background service worker.

const NATIVE_HOST_NAME = "com.vaulttube.host";

function connectToHost() {
  return chrome.runtime.connectNative(NATIVE_HOST_NAME);
}

function sendRequest(command, params = {}) {
  return new Promise((resolve, reject) => {
    chrome.runtime.sendNativeMessage(
      NATIVE_HOST_NAME,
      { command, params },
      (response) => {
        if (chrome.runtime.lastError) {
          reject(new Error(chrome.runtime.lastError.message));
          return;
        }
        if (!response || !response.ok) {
          reject(new Error(response && response.error ? response.error : "Unknown error."));
          return;
        }
        resolve(response.result);
      }
    );
  });
}
