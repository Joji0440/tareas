const express = require('express');
const { ApolloServer } = require('apollo-server-express');
const typeDefs = require('./schema');
const resolvers = require('./resolvers');

// Función principal para iniciar el servidor
async function iniciarServidor() {
  const app = express();
  const servidor = new ApolloServer({ typeDefs, resolvers });

  await servidor.start();
  servidor.applyMiddleware({ app });

  app.listen(4000, () =>
    console.log(`🚀 Servidor listo en http://localhost:4000${servidor.graphqlPath}`)
  );
}

iniciarServidor();
