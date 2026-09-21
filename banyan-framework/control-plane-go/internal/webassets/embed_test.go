package webassets

import (
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"testing"
)

func TestEmbeddedAssetManifest(t *testing.T) {
	data, err := Dist.ReadFile("dist/asset-manifest.json")
	if err != nil {
		t.Fatal(err)
	}
	var manifest struct {
		Assets []struct{ Path, SHA256 string } `json:"assets"`
	}
	if err := json.Unmarshal(data, &manifest); err != nil {
		t.Fatal(err)
	}
	if len(manifest.Assets) == 0 {
		t.Fatal("empty asset manifest")
	}
	for _, item := range manifest.Assets {
		asset, err := Dist.ReadFile("dist/" + item.Path)
		if err != nil {
			t.Fatal(err)
		}
		sum := sha256.Sum256(asset)
		if hex.EncodeToString(sum[:]) != item.SHA256 {
			t.Fatalf("hash mismatch: %s", item.Path)
		}
	}
}
