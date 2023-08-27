// Fetch and parse the rss_feed.xml file
fetch('https://raw.githubusercontent.com/ChandanShakya/Kurakahani/main/rss_feed.xml')
    .then(response => response.text())
    .then(data => {
        const parser = new DOMParser();
        const xml = parser.parseFromString(data, 'application/xml');

        const itunesNamespace = 'http://www.itunes.com/dtds/podcast-1.0.dtd';

        // Loop through each <item> element and create a list item
        const items = xml.querySelectorAll('item');
        const episodesContainer = document.getElementById('episodes');

        items.forEach(item => {
            const title = item.querySelector('title').textContent;
            const description = item.querySelector('description').textContent;

            const itunesNamespace = 'http://www.itunes.com/dtds/podcast-1.0.dtd';
            const imageElement = item.getElementsByTagNameNS(itunesNamespace, 'image')[0];
            const image = imageElement ? imageElement.getAttribute('href') : '';

            const audioUrl = item.querySelector('enclosure').getAttribute('url');

            // Split description into lines and create line breaks
            const descriptionLines = description.split('\n').filter(line => line.trim() !== '');
            const formattedDescription = descriptionLines.map(line => {
                return line.replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank">$1</a>');
            }).join('<br>');

            const filename = audioUrl.substring(audioUrl.lastIndexOf('/') + 1, audioUrl.lastIndexOf('.'));
            const youtubeVideoUrl = `https://www.youtube.com/watch?v=${filename}`;

            // Create the episode card HTML
            const episodeHTML = `
                <div class="card mb-3">
                <a href="${youtubeVideoUrl}" target="_blank">
                    <img src="${image}" class="card-img-top" alt="${title} Episode Image">
                </a>
                    <div class="card-body">
                        <h5 class="card-title">${title}</h5>
                        <p class="card-text">${formattedDescription}</p>
                        <audio controls class="w-100">
                            <source src="${audioUrl}" type="audio/mpeg">
                            Your browser does not support the audio element.
                        </audio>
                    </div>
                </div>
            `;

            // Append the episode card to the episodes container
            episodesContainer.innerHTML += episodeHTML;
        });
    })
    .catch(error => {
        console.error('Error fetching rss_feed.xml:', error);
    });
