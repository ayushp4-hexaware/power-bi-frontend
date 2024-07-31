import React, { useState, useEffect } from 'react';
import { PowerBIEmbed } from 'powerbi-client-react';
import { models } from 'powerbi-client';
import { fetchEmbedInfo } from '../api_service/powerbi-api.js';

const PowerBIReport = () => {
  const [embedConfig, setEmbedConfig] = useState(null);

  useEffect(() => {
    const loadEmbedInfo = async () => {
      try {
        const embedInfo = await fetchEmbedInfo();
        setEmbedConfig({
          type: 'report',
          id: embedInfo.reportID, // Optionally set dynamically
          embedUrl: embedInfo.embedUrl,
          accessToken: embedInfo.embedToken,
          tokenType: models.TokenType.Embed,
          settings: {
            panes: {
              filters: {
                visible: false,
                expanded: false
              }
            }
          }
        });
      } catch (error) {
        console.error('Error loading embed info:', error);
      }
    };

    loadEmbedInfo();
  }, []);

  return (
    <div>
      <h1>Power BI Report</h1>
      {embedConfig ? (
        <PowerBIEmbed
          embedConfig={embedConfig}
          cssClassName={'embed-container'}
          getEmbeddedComponent={(embedObject) => {
            console.log('Embedded Report:', embedObject);
          }}
        />
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default PowerBIReport;
