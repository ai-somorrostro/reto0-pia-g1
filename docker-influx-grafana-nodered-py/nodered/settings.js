    module.exports = {
        flowFile: 'flows.json',
        credentialSecret: false,   // Desactiva cifrado para usar el cred.json plano
        uiPort: process.env.PORT || 1880,
        httpAdminRoot: '/',
        httpNodeRoot: '/',
    };
