var crypto = require("crypto");
var path = require("path");
var fs = require("fs");

var encryptStringWithRsaPublicKey = function(toEncrypt, publicKey) {
    var buffer = Buffer.from(toEncrypt);
    console.log("public key", publicKey)
    var pk = {
        key: publicKey
    }
    var encrypted = crypto.publicEncrypt(publicKey, buffer);
    return encrypted.toString("base64");
};

module.exports = {
    encryptStringWithRsaPublicKey: encryptStringWithRsaPublicKey,
}