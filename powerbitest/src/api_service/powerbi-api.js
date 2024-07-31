const API_URL = 'http://localhost:3005';

export async function fetchEmbedInfo() {
  try {
    const response = await fetch(`${API_URL}/embed-info`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching embed info:', error);
    throw error;
  }
}
