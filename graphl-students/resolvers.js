const estudiantes = [];
let contadorId = 1;

const resolvers = {
  Query: {
    // Devuelve todos los estudiantes
    estudiantes: () => estudiantes,
    // Devuelve un estudiante por su ID
    estudiante: (_, { id }) => estudiantes.find(e => e.id === id),
  },
  Mutation: {
    // Agrega un nuevo estudiante
    agregarEstudiante: (_, { nombre, edad }) => {
      const nuevoEstudiante = { id: String(contadorId++), nombre, edad };
      estudiantes.push(nuevoEstudiante);
      return nuevoEstudiante;
    },
  },
};

module.exports = resolvers;
