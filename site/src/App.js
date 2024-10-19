import './App.css';
import { Helmet } from 'react-helmet';
import { Button, createTheme, Stack, ThemeProvider, Typography } from '@mui/material';
import { Upload } from '@mui/icons-material';

function App() {
  const theme = createTheme({
    typography: {
      fontFamily: [
        "Inter"
      ].join(" ")
    },
    components: {
      MuiCssBaseline: {
        styleOverrides: `
          @font-face {
            @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
            font-family: 'Inter';
            font-style: normal;
            font-display: swap;
            font-weight: 400;
          }
        `,
      },
      MuiButton: {
        styleOverrides: {
          root: {
            border: "1px solid #505050",
            borderRadius: "0.5rem"
          }
        }
      }
    },
    palette: {
      mode: 'dark'
    }
  });

  return (
    <ThemeProvider theme={theme}>
      <div className="App">
        <Helmet>
          <title>treetastic</title>
          <link rel="preconnect" href="https://fonts.googleapis.com" />
          <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
          <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet"></link>
        </Helmet>
        <main>
          <Stack direction="column" spacing={2} justifyContent="space-between" height="100%">
            <Stack direction="column" spacing={2}>
              <Typography variant="h3" fontWeight={600}>treetastic</Typography>
              <Typography variant="h6" fontWeight={500} color="#b2b2b2">optimised planting of trees in cities</Typography>
              <Button>
                <div className="uploadImages">
                  <Upload />
                  <Typography variant="p" fontWeight={500} fontSize="1.3rem">Upload images</Typography>
                </div>
              </Button>
            </Stack>
            <div>
            <Typography variant="p" fontWeight={500} marginTop="1rem" color="#b2b2b2">by <a href="https://github.com/ThatJammyDodger" target="_blank" rel="noreferrer" color="#9a72cf">Jay Ambadkar</a>, <a href="https://github.com/sd0e" target="_blank" rel="noreferrer" color="#9a72cf">Sebastian Doe</a>, <s>Daniel Fostiak and Yuvraj Singh</s></Typography>
            </div>
          </Stack>
        </main>
      </div>
    </ThemeProvider>
  );
}

export default App;
