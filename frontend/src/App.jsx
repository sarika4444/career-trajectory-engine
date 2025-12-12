import React, { useState } from "react";

export default function App() {
  const [skills, setSkills] = useState("python, git, sql");
  const [title, setTitle] = useState("Junior Software Engineer");
  const [seniority, setSeniority] = useState("Junior");
  const [years, setYears] = useState(1);
  const [results, setResults] = useState(null);

  async function submit(e) {
    e.preventDefault();

    const payload = {
      current_title: title,
      current_seniority: seniority,
      skills: skills.split(",").map((s) => s.trim()),
      years_experience: Number(years),
    };

   const res = await fetch("/profile", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(payload),
});


    setResults(await res.json());
  }

  return (
    <div className="min-h-screen p-8 bg-gray-100">
      <div className="max-w-xl mx-auto p-6 bg-white rounded-md shadow">
        <h1 className="text-2xl font-bold mb-4">Career Trajectory Engine</h1>

        <form className="space-y-4" onSubmit={submit}>
          <div>
            <label className="text-sm font-medium">Current Title</label>
            <input
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="w-full border p-2 rounded"
            />
          </div>

          <div>
            <label className="text-sm font-medium">Seniority</label>
            <input
              type="text"
              value={seniority}
              onChange={(e) => setSeniority(e.target.value)}
              className="w-full border p-2 rounded"
            />
          </div>

          <div>
            <label className="text-sm font-medium">Skills (comma separated)</label>
            <input
              value={skills}
              onChange={(e) => setSkills(e.target.value)}
              className="w-full border p-2 rounded"
            />
          </div>

          <div>
            <label className="text-sm font-medium">Years of Experience</label>
            <input
              type="number"
              value={years}
              onChange={(e) => setYears(e.target.value)}
              className="w-full border p-2 rounded"
            />
          </div>

          <button
            type="submit"
            className="w-full bg-blue-600 hover:bg-blue-700 text-white p-2 rounded mt-2"
          >
            Generate Career Path
          </button>
        </form>

        {results && (
          <div className="mt-6 p-4 border rounded bg-gray-50">
            <h2 className="text-xl font-semibold mb-2">Output</h2>
            <pre className="whitespace-pre-wrap text-sm">
              {JSON.stringify(results, null, 2)}
            </pre>
          </div>
        )}
      </div>
    </div>
  );
}
