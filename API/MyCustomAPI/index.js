//CREDIT: https://github.com/Senither/hypixel-skyblock-facade (Modified)
const FetchurRoute = require('./routes/v1/fetchur');
const ProfileRoute = require('./routes/v1/profile');
const ProfilesRoute = require('./routes/v1/profiles');
const ProfileItemsRoute = require('./routes/v1/profileItems');
const ProfilesItemsRoute = require('./routes/v1/profilesItems');
const ProfileV2Route = require('./routes/v2/profile');
const ProfilesV2Route = require('./routes/v2/profiles');
const NetworthRoute = require('./routes/v2/networth');
const ItemNetworthRoute = require('./routes/v2/itemNetworth');
const NotFound = require('./middleware/notfound');
const Auth = require('./middleware/auth');
const ErrorHandler = require('./middleware/errorhandler');
const rateLimit = require('express-rate-limit');
const express = require('express');
const app = express();
const refreshCollections = require('./data/refreshCollections');
const { refreshPrices } = require('./data/refreshPrices');
require('dotenv').config();
const port = 8000

process.on('uncaughtException', (error) => console.log(error));
process.on('unhandledRejection', (error) => console.log(error));

const limiter = rateLimit({
    windowMs: 1000 * 60, // 1 minute
    max: 60,
    standardHeaders: true,
    legacyHeaders: false,
    message: {
        status: 429,
        message: 'Too many requests, please try again later.',
    },
});

app.use(express.static(__dirname + '/public'));
app.use(limiter);
app.use(require('cors')());
app.use(express.json({ limit: '15mb' }));
app.use(express.urlencoded({ extended: true }));

app.get('/v1/fetchur', FetchurRoute);
app.get('/v1/profile/:uuid/:profileid', ProfileRoute);
app.get('/v1/profiles/:uuid', ProfilesRoute);
app.get('/v1/items/:uuid/:profileid', ProfileItemsRoute);
app.get('/v1/items/:uuid', ProfilesItemsRoute);

app.get('/v2/profile/:uuid/:profileid', ProfileV2Route);
app.get('/v2/profiles/:uuid', ProfilesV2Route);
app.post('/v2/networth', NetworthRoute);
app.post('/v2/networth/item', ItemNetworthRoute);

app.use(NotFound);
app.use(ErrorHandler);

refreshCollections();
refreshPrices();


app.listen(port, () => {
    console.log(`Now listening on port ${port}`);
});