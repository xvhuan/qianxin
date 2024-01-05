const crypto = require("crypto-js");
window = global
const NodeRSA = require('jsencrypt');

function short() {
    for (var e = "", a = 0; a < 32; a++)
        e += Math.floor(16 * Math.random()).toString(16);
    return e
}

function password(e, a) {
    var c = a.substring(0, 16);
    a = crypto.enc.Utf8.parse(a),
        c = crypto.enc.Utf8.parse(c),
        e = "string" === typeof e ? e : JSON.stringify(e);
    var t = crypto.AES.encrypt(e, a, {
        iv: c,
        mode: crypto.mode.CBC,
        padding: crypto.pad.Pkcs7
    });
    return t.toString()
}

function key_iv(e, a) {
    var c = a.substring(0, 16);
    a = crypto.enc.Utf8.parse(a),
        c = crypto.enc.Utf8.parse(c);
    var t = {
        key: crypto.enc.Base64.stringify(a),
        iv: crypto.enc.Base64.stringify(c)
    };
    t = JSON.stringify(t)
    var aa = new NodeRSA()
    aa.setPublicKey(e);
    return aa.encrypt(t)
}

