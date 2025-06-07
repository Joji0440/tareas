const { gql } = require('apollo-server-express');

const typeDefs = gql`
  type Estudiante {
    id: ID!
    nombre: String!
    edad: Int!
  }

  type Query {
    estudiantes: [Estudiante]
    estudiante(id: ID!): Estudiante
  }

  type Mutation {
    agregarEstudiante(nombre: String!, edad: Int!): Estudiante
    updateEstudiante(id: ID!, nombre: String, edad: Int): Estudiante
    eliminarEstudiante(id: ID!): Boolean
  }
`;

module.exports = typeDefs;
