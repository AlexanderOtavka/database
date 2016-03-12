'use strict';
// `app` is automatically added to global scope

if (window.location.hash === "#refresh") {
  window.location.href = "/";
}

app.sendName = function () {
  app.$.ajax.generateRequest();
  console.log(app.name);
};

app.getMessageBody = function (name) {
  return {
    name: name,
  };
};
