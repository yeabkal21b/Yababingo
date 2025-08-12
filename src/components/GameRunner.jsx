export function speakNumberAmharic(number, gender = "female") {
  const utter = new window.SpeechSynthesisUtterance(`${number}`);
  utter.lang = "am-ET";
  // Voice selection (optional, browser dependent)
  const voices = window.speechSynthesis.getVoices();
  let amharicVoice = voices.find(
    (v) => v.lang === "am-ET" && v.name.includes(gender === "male" ? "Male" : "Female")
  );
  if (amharicVoice) utter.voice = amharicVoice;
  window.speechSynthesis.speak(utter);
}

// In your game runner, call speakNumberAmharic(calledNumber, gender) when a number is called.