const App = () => {
  return (
    <div>
      <Tweet
        name="Todd Jackson"
        username="tj"
        date={new Date().toDateString()}
        message="This is my first teweet!"
      />
      <Tweet
        name="Joe L"
        username="joel"
        date={new Date().toDateString()}
        message="I love music!"
      />
      <Tweet
        name="Sasha Buford"
        username="sashafierce"
        date={new Date().toDateString()}
        message="Follow me to here and instagram!"
      />
    </div>
  );
};
