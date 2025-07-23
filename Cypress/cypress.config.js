const { defineConfig } = require("cypress");
const createBundler = require("@bahmutov/cypress-esbuild-preprocessor");
const preprocessor = require("@badeball/cypress-cucumber-preprocessor");
const createEsbuildPlugin = require("@badeball/cypress-cucumber-preprocessor/esbuild");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      on("file:preprocessor",
      createBundler({
        plugins: [createEsbuildPlugin.default(config)],
      }));
      on('before:browser:launch', (browser = {}, launchOptions) => {
        if (browser.family === 'chromium' && browser.name !== 'electron') {
          launchOptions.args.push('--disable-features=PasswordLeakDetection')
          return launchOptions
        }
      })
      preprocessor.addCucumberPreprocessorPlugin(on, config);
      return config;
    },
    viewportWidth: 1920,
    viewportHeight: 1080,
    specPattern: "**/*.feature",
    baseUrl: "https://opensource-demo.orangehrmlive.com/",
  },
})
