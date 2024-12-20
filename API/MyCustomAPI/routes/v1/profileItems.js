//CREDIT: https://github.com/Senither/hypixel-skyblock-facade (Modified)
const { isUuid } = require('../../utils/uuid');
const { makeRequest, wrap } = require('../../utils/request');
const { parseProfileItems, parseHypixel } = require('../../utils/hypixel');
require('dotenv').config();
const mySecret = process.env['HYPIXEL_API_KEY']

module.exports = wrap(async function (req, res) {
    const profileid = req.params.profileid;
    let uuid = req.params.uuid;
    if (!isUuid(uuid)) {
        const mojang_response = await makeRequest(res, `https://api.ashcon.app/mojang/v2/user/${uuid}`);
        if (mojang_response?.data?.uuid) {
            uuid = mojang_response.data.uuid.replace(/-/g, '');
        }
    }

    const playerRes = await makeRequest(res, `https://api.hypixel.net/player?key=e2a42c13-f139-4190-b850-6d0613e6d2fa&uuid=${uuid}`);
    const player = parseHypixel(playerRes, uuid, res);

    const profileRes = await makeRequest(res, `https://api.hypixel.net/skyblock/profiles?key=e2a42c13-f139-4190-b850-6d0613e6d2fa&uuid=${uuid}`);
    const profile = await parseProfileItems(player, profileRes, uuid, profileid, res);
    console.log(mySecret)
    return res.status(200).json({ status: 200, data: profile });
});