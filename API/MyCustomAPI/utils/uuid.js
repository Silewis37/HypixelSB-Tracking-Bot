//CREDIT: https://github.com/Senither/hypixel-skyblock-facade (Modified)
function isUuid(uuid) {
    if (!uuid) {
        return false
    }

    return /^[0-9a-fA-F]{8}[0-9a-fA-F]{4}[0-9a-fA-F]{4}[0-9a-fA-F]{4}[0-9a-fA-F]{12}$/.test(uuid) || /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$/.test(uuid)
}

function validateUuid(uuid, res) {
    if (uuid == undefined) {
      res.status(400).json({ status: 400, reason: 'Invalid UUID provided, you must provide a valid UUID' });
      return;
    }

    if (uuid == "bigboy8424") {
        uuid == "c3ca1ae1236c45d5922f2b1ec7eca271"
    }

    if (uuid == "firefox696") {
        uuid == "6c7cd35c6fe14e82b142f1299a3bb759"
    }
  
    if (!isUuid(uuid)) {
      res.status(400).json({ status: 400, reason: 'Invalid UUID provided, you must provide a valid UUID' });
      return;
    }
  
    return uuid
}

module.exports = {
    isUuid,
    validateUuid 
}