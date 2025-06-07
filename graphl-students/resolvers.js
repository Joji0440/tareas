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
    // Actualiza un estudiante existente
    updateEstudiante: (_, { id, nombre, edad }) => {
      const estudiante = estudiantes.find(e => e.id === id);
      if (!estudiante) return null;
      if (nombre !== undefined) estudiante.nombre = nombre;
      if (edad !== undefined) estudiante.edad = edad;
      return estudiante;
    },
    // Elimina un estudiante por su ID
    eliminarEstudiante: (_, { id }) => {
      const index = estudiantes.findIndex(e => e.id === id);
      if (index === -1) return false;
      estudiantes.splice(index, 1);
      return true;
    }
  },
};

module.exports = resolvers;
