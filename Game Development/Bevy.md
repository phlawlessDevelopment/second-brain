---
date created: Monday, November 7th 2022, 2:26:23 pm
date modified: Tuesday, November 8th 2022, 5:27:06 pm
date_created: Monday, November 7th 2022, 2:26:23 pm
date_modified: Tuesday, November 8th 2022, 5:30:19 pm
---
#rust #gamedev/engine  #gamedev/tooling 

Data oriented game engine written in [[Rust]]

## Snippets

#### camera plugin
```rust
use bevy::prelude::*;

pub struct CameraPlugin;

#[derive(Component)]
pub struct MainCamera;

fn setup(mut commands: Commands) {
	commands
	.spawn_bundle(Camera2dBundle::default())
	.insert(MainCamera);
}

impl Plugin for CameraPlugin {
	fn build(&self, app: &mut App) {
		app.add_startup_system_to_stage(StartupStage::PreStartup, setup);
	}

}

```
