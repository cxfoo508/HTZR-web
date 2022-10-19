import getConfig from "next/config";

let publicRuntimeConfig: any;

if (typeof getConfig !== "undefined") {
  publicRuntimeConfig = getConfig()?.publicRuntimeConfig;
} else {
  publicRuntimeConfig = undefined
}
const config = {
  devUrl: publicRuntimeConfig?.devUrl ?? "",
};

export default config