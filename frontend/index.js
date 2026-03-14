const button = document.getElementById("submit");

async function loadBlogs() {
  const blogContainer = document.getElementById("blog-container");
  try {
    const response = await fetch("http://127.0.0.1:8000/blogs");
    const blogs = await response.json();

    blogContainer.innerHTML = "";

    if (blogs.length === 0) {
      blogContainer.innerHTML = "<p>No blogs yet.</p>";
      return;
    }

    blogs.forEach(blog => {
      const card = document.createElement("div");
      card.innerHTML = `
        <h3>${blog.title}</h3>
        <p>${blog.content}</p>
        <small>By ${blog.author.name} — ${blog.author.joined}</small>
        <hr>
      `;
      blogContainer.appendChild(card);
    });

  } catch (err) {
    console.error("Error loading blogs:", err);
  }
}

loadBlogs();

button.addEventListener("click", async () => {
  const title = document.querySelector('input[placeholder="title"]').value;
  const content = document.querySelector('input[placeholder="content"]').value;

  if (!title || !content) {
    alert("Please fill in both fields.");
    return;
  }

  const blog = {
    id: crypto.randomUUID().slice(0, 3),
    title,
    content,
    author: {
      id: 1,
      name: "Dev",
      joined: "2001-12-04",
      email: "SomeoneSomeone@gmail.com"
    }
  };

  try {
    const response = await fetch("http://127.0.0.1:8000/write_blog", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(blog)
    });

    await response.json();
    alert("Blog posted successfully!");
    loadBlogs(); 

  } catch (err) {
    console.error("Error:", err);
    alert("Failed to post blog.");
  }
});