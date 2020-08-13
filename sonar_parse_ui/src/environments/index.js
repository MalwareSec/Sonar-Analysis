import { devConfig } from "./dev.js";

export default function setEnvironments() {
    if (process.env.REACT_APP_ENV === "dev") {
        return devConfig;
    }
}