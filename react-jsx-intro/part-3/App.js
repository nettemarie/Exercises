const App = () => {
  return (
    <div>
      <Person
        name="Jerry"
        age={32}
        hobbies={["basketball", "watching tv", "football"]}
      />
      <Person name="Denise" age={28} hobbies={["writing", "reading"]} />
      <Person name="Juan" age={12} hobbies={["drumming", "baseball"]} />
      <Person
        name="Judy"
        age={42}
        hobbies={["reading", "teaching", "running"]}
      />
    </div>
  );
};
