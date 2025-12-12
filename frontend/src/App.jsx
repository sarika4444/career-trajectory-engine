// frontend/src/App.jsx
import React, { useState } from "react";

export default function App() {
  const [skills, setSkills] = useState("python, git, sql");
  const [title, setTitle] = useState("Junior Software Engineer");
  const [seniority, setSeniority] = useState("Junior");
  const [years, setYears] = useState(1);
  const [targetRole, setTargetRole] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  async function submit(e) {
    e && e.preventDefault();
    setLoading(true);
    const payload = {
      current_title: title,
      current_seniority: seniority,
      skills: skills.split(",").map((s) => s.trim()),
      years_experience: Number(years),
      target_role: targetRole || undefined
    };
    try {
     const res = await fetch("http://localhost:8000/profile", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
});

      
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
      alert("Error contacting backend");
    } finally {
      setLoading(false);
    }
  }

  function SkillList({items}) {
    if(!items || items.length === 0) return <span className="text-sm text-gray-500">—</span>;
    return <ul className="list-disc ml-5 space-y-1 text-sm">{items.map((s,i)=>(<li key={i}>{s}</li>))}</ul>;
  }

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-5xl mx-auto">
        <header className="flex items-center justify-between mb-6">
          <h1 className="text-2xl font-bold">Career Trajectory Engine</h1>
          <div className="text-sm text-gray-600">Prototype • Skill-gap • Tracks • Salary</div>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <form className="bg-white p-6 rounded-lg shadow-sm space-y-4" onSubmit={submit}>
            <h2 className="font-semibold text-lg">Your profile</h2>

            <label className="block text-sm">Current Title</label>
            <input value={title} onChange={(e)=>setTitle(e.target.value)} className="w-full border p-2 rounded" />

            <label className="block text-sm">Seniority</label>
            <input value={seniority} onChange={(e)=>setSeniority(e.target.value)} className="w-full border p-2 rounded" />

            <label className="block text-sm">Skills (comma separated)</label>
            <input value={skills} onChange={(e)=>setSkills(e.target.value)} className="w-full border p-2 rounded" />

            <label className="block text-sm">Years of Experience</label>
            <input type="number" value={years} onChange={(e)=>setYears(e.target.value)} className="w-full border p-2 rounded" />

            <label className="block text-sm">Optional target role</label>
            <input value={targetRole} onChange={(e)=>setTargetRole(e.target.value)} placeholder="Associate Software Engineer" className="w-full border p-2 rounded" />

            <button type="submit" disabled={loading} className="w-full bg-indigo-600 hover:bg-indigo-700 text-white p-2 rounded mt-2">
              {loading ? "Working..." : "Generate Trajectory"}
            </button>
          </form>

          <div className="lg:col-span-2 space-y-6">
            <div className="bg-white p-6 rounded-lg shadow-sm">
              <h3 className="font-semibold">Suggested Next Roles</h3>
              {!result && <div className="text-sm text-gray-500 mt-2">No suggestions yet — submit your profile.</div>}
              {result && result.suggestions && (
                <div className="mt-3 grid grid-cols-1 md:grid-cols-2 gap-4">
                  {result.suggestions.map((s,idx)=>(
                    <div key={idx} className="border p-4 rounded">
                      <div className="flex items-center justify-between">
                        <div>
                          <div className="font-bold">{s.title}</div>
                          <div className="text-xs text-gray-500">{s.seniority} • Score: {s.score}</div>
                        </div>
                        <div className="text-sm text-gray-700">{s.salary_range}</div>
                      </div>
                      <div className="mt-3">
                        <div className="text-sm font-semibold">Missing skills</div>
                        <SkillList items={s.missing_skills} />
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>

            <div className="bg-white p-6 rounded-lg shadow-sm">
              <h3 className="font-semibold">Top role & Skill-gap</h3>
              {!result && <div className="text-sm text-gray-500 mt-2">—</div>}
              {result && (
                <div className="mt-3 grid grid-cols-1 md:grid-cols-3 gap-4">
                  <div>
                    <div className="text-xs text-gray-500">Top Role</div>
                    <div className="font-bold">{result.top_role}</div>
                    <div className="text-sm mt-1">Salary range: <span className="font-semibold">{result.salary_estimate_for_top_role}</span></div>
                  </div>
                  <div>
                    <div className="text-xs text-gray-500">Skill-gap to top role</div>
                    <SkillList items={result.skill_gap} />
                  </div>
                  <div>
                    <div className="text-xs text-gray-500">Recommended skills (priority)</div>
                    <SkillList items={result.recommended_skills} />
                  </div>
                </div>
              )}
            </div>

            <div className="bg-white p-6 rounded-lg shadow-sm">
              <h3 className="font-semibold">Career Tracks</h3>
              {!result && <div className="text-sm text-gray-500 mt-2">—</div>}
              {result && result.career_tracks && (
                <div className="mt-3 space-y-3">
                  {Object.entries(result.career_tracks).map(([trackName, seq], idx)=>(
                    <div key={idx} className="p-3 border rounded">
                      <div className="font-semibold">{trackName} track</div>
                      <div className="text-sm text-gray-600 mt-1">{seq.join(" → ")}</div>
                    </div>
                  ))}
                </div>
              )}
            </div>

          </div>
        </div>

      </div>
    </div>
  );
}
