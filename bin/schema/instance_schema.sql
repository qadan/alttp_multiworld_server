/**
 * Clean up first.
 */
drop table if exists multiworld_instances;

/**
 * Multiworld instances.
 *
 * Including:
 *  * 'instance_id' (int): The unique identifier of the instance.
 *  * 'timestamp' (int): Unix timestamp of the instance creation.
 *  * 'datafile_uri' (string): URI of the instance datafile.
 *  * 'savefile_uri' (string): URI of the instance savefile.
 *  * 'autopurge_session' (bool): Whether to automatically purge the session
 *    after the configured timeout.
 *  * 'autopurge_files' (bool): Whether to automatically purge the files if the
 *    session is closed.
 *  * 'process_id': (int) ID of the running server process.
 */
create table multiworld_instances (
  id integer primary key autoincrement not null,
  timestamp integer not null,
  datafile_uri text not null,
  savefile_uri text not null,
  autopurge_session boolean not null,
  autopurge_files boolean not null,
  process_id integer not null,
);
