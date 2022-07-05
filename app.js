import { visualDomDiff } from "visual-dom-diff";
import jquery from "jquery";

jquery(document).ready(() => {
  fetch("/en/latest/index.html")
    .then((response) => response.text())
    .then((text) => {
      const parser = new DOMParser();
      const htmlDocument = parser.parseFromString(text, "text/html");
      const old_body = htmlDocument.documentElement.querySelector("body");

      const new_body = jquery("body")[0];

      const diffNode = visualDomDiff(old_body, new_body);

      jquery("body").html(diffNode);

      jquery(".vdd-added").css("background-color", "#52e80f96");
      jquery(".vdd-removed").css("background-color", "#f94532ab");
    });
});
